import java.io.*;
import java.lang.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.jar.*;
import java.util.zip.ZipEntry;
import java.text.Collator;

/**
* Builds Api file for use with SciTe.<br>
* Note: Classes to be processed must be in your CLASSPATH<br>
*
* @author <a href="mailto:nazimok@yahoo.com">Alex Nazimok</a>
* @version 1.1
*/
public class ApiBuilder
{
    private static ArrayList fileList = new ArrayList();
    private static boolean appendToFile = false;
    private static boolean isJar = false;
    private static final int MAX_OPTIONS = 2;

	/**
	* main method
	*/
    public static void main(String args[])
        throws Exception
    {
        ApiBuilder apiB = new ApiBuilder();

        if (args.length < 2)
           printUsage();

        int argNum = 0;
        for(int i = 0; i < MAX_OPTIONS; i++)
        {
            if(args[i].equals("-a"))
            {
                appendToFile = true;
                argNum++;
            }

            if(args[i].equals("-j"))
            {
                isJar = true;
                argNum++;
            }

            if(args[i].equals("-s"))
            {
                apiB.sortApiFile(args[1]);
                return;
            }
        }

        System.out.println("\n-----------------------------------------------");
        System.out.println("Starting processing...");
        if(!isJar)
            apiB.buildFileList(new File(args[argNum]));
        else
            apiB.processJar(args[argNum]);

        apiB.writeToFile(args[argNum], args[++argNum]);
        System.out.println("Done...");
        System.out.println("-----------------------------------------------\n");
    }

    /**
	* Creates a list of all of the methods for basedir .class files.
    * TODO: I am not sure at this point what the best way to handle inner
    * classes is so I am just replacing '$' with '.'
	*/
	private List buildMethodList(String baseDir)
        throws Exception
    {
        List methodList = new ArrayList();

        for (int i = 0; i < fileList.size(); i++)
        {
            String className = formatClassName(fileList.get(i).toString(), baseDir);

            Class clazz = getClass().getClassLoader().loadClass(className);

            if (clazz != null)
            {
                Method methods[] = clazz.getMethods();

                for (int j = 0; j < methods.length; j++)
                {
                    String sig = (methods[j].getName()).replace('$', '.') + "(";
                    Class[] params = methods[j].getParameterTypes();

                    for (int k = 0; k < params.length; k++)
                        sig += formatParams(params[k].getName());

                    if (sig.lastIndexOf(",") == sig.length() - 1)
                        sig = sig.substring(0, sig.length() - 1);

                    sig += ")";
                    if (!methodList.contains(sig))
                        methodList.add(sig);
                }
            }
        }
        return methodList;
    }

    /**
	* Creates a list of all of the constructors for basedir .class files.
	*/
    private List buildConstructorList(String baseDir)
        throws Exception
    {
        List methodList = new ArrayList();

        for (int i = 0; i < fileList.size(); i++)
        {
            String className = formatClassName(fileList.get(i).toString(), baseDir);

            Class clazz = getClass().getClassLoader().loadClass(className);

            if (clazz != null)
            {
                String packName = null;
                try{packName = clazz.getPackage().getName();}
                catch(Exception e){}

                Constructor methods[] = clazz.getConstructors();

                for (int j = 0; j < methods.length; j++)
                {
                    String constName = (methods[j].getName()).replace('$', '.');

                    if (packName != null && packName.length() > 0)
                        constName = constName.substring(constName.indexOf(packName) + packName.length() + 1);

                    String sig = constName + "(";
                    Class[] params = methods[j].getParameterTypes();

                    for (int k = 0; k < params.length; k++)
                        sig += formatParams(params[k].getName());

                    if (sig.lastIndexOf(",") == sig.length() - 1)
                        sig = sig.substring(0, sig.length() - 1);

                    sig += ")";
                    if (!methodList.contains(sig))
                        methodList.add(sig);
                }
            }
        }
        return methodList;
    }

	/**
	* Replaces arrays classloader representation with real values
	*/
    private String formatParams(String paramName)
    {
        String name = "";

        if (paramName.startsWith("[B"))
            name = "byte[],";
        else if (paramName.startsWith("[C"))
            name = "char[],";
        else if (paramName.startsWith("[D"))
            name = "double[],";
        else if (paramName.startsWith("[F"))
            name = "float[],";
        else if (paramName.startsWith("[I"))
            name = "int[],";
        else if (paramName.startsWith("[J"))
            name = "long[],";
        else if (paramName.startsWith("[S"))
            name = "short[],";
        else if (paramName.startsWith("[Z"))
            name = "boolean[],";
        else if (paramName.startsWith("[L"))
            name = paramName.substring(2, paramName.indexOf(";")) + "[],";
        else
            name = paramName + ",";

        return name.replace('$', '.');
    }

    /**
	* Sorts methods and constructors lists and writes them to file.
	*/
	private void writeToFile(String baseDir, String outputFile)
        throws Exception
    {
        RandomAccessFile output = new RandomAccessFile(outputFile, "rw");

        if (appendToFile)
            output.seek(output.length());

        PrintWriter bw = new PrintWriter(new FileWriter(output.getFD()));
        List methodList = buildMethodList(baseDir);
        List constructorList = buildConstructorList(baseDir);
        List all = new ArrayList();

        all.addAll(methodList);
        all.addAll(constructorList);

        Collections.sort(all, new CaseCompareator());

        for (int j = 0; j < all.size(); j++)
        {
            bw.println((String) all.get(j));
            bw.flush();
        }

        bw.close();
    }

    /**
	* Builds list of .class files to be processed (recursively)
	*/
	private void buildFileList(File baseDir)
    {
        String files[] = baseDir.list();

        if(files == null || files.length == 0)
        {
            System.out.println("\nUnable to find .class files in " + baseDir);
            printUsage();
        }

        for (int i = 0; i < files.length; i++)
        {
            File f = new File(baseDir, files[i]);

            if (f.isDirectory())
                buildFileList(f);
            if (f.getName().endsWith(".class"))
                if (!fileList.contains(f))
                    fileList.add(f);
        }
    }

	/**
	* Builds a className from filename passed in.
	* @param f File to be processed
	* @param baseDir based directory for the file being processed.
	* It is stripped out from class name.
	* @return className
	*
	*/
    private String formatClassName(String fileName, String baseDir)
    {
        fileName = fileName.replace('\\', '/');
        if(!isJar)
            fileName = fileName.substring(fileName.indexOf(baseDir) + baseDir.length(), fileName.indexOf(".class"));
        else
            fileName = fileName.substring(0, fileName.indexOf(".class"));

        fileName = fileName.replace('/', '.');
        return (fileName.startsWith(".") ? fileName.substring(1) : fileName);
    }

    /**
    * Builds list of files from Jar File.
    * Jar File must be in your CLASSPATH
    */
    private void processJar(String jarFile)
        throws Exception
    {
        JarFile jar = new JarFile(jarFile);
        for(Enumeration e = jar.entries(); e.hasMoreElements();)
        {
            String fileName = ((ZipEntry)e.nextElement()).getName();
            if(fileName.endsWith(".class"))
                if(!fileList.contains(fileName))
                    fileList.add(fileName);
        }
    }

    private static void printUsage()
    {
        System.out.println("\nUsage: ApiBuilder [option] <baseDir | jarFile> <output file>");
        System.out.println("OR");
        System.out.println("Usage: ApiBuilder -s <api filename>");
        System.out.println("Options:");
        System.out.println("\t-a: Appends to existing file");
        System.out.println("\t-j: Processes jar file");
        System.out.println("\t-s: Sorts api file. Removes duplicate entry");
        System.exit(1);
    }

    private class CaseCompareator implements java.util.Comparator
    {

        /**
         *	Compare two objects and...
         *
         *	  return an integer < 1 if o1 is "less" than o2
         *	  return  0 if o1 and o2 are "equal"
         *	  return an integer > 1 if o1 is "greater" than o2
         *
         */
        public int compare(Object o1, Object o2)
        {
            if (o1 instanceof String && o2 instanceof String)
                return o1.toString().compareToIgnoreCase(o2.toString());
            else
                return Collator.getInstance().compare(o1, o2);
        }
    }

    /**
    * Sorts api file removes duplicate entries.
    */
    private void sortApiFile(String apiFile)
        throws Exception
    {

        File oldFile = new File(apiFile);
        BufferedReader br = new BufferedReader(new FileReader(oldFile));
        String line = new String();
        List lines = new ArrayList();

        while((line = br.readLine()) != null)
            if(!lines.contains(line))
                lines.add(line);

        br.close();
        oldFile.delete();

        Collections.sort(lines, new CaseCompareator());


        File newFile = new File(apiFile);
        PrintWriter out = new PrintWriter(new FileOutputStream(newFile));

        for(int i = 0; i < lines.size(); i++)
            out.println(lines.get(i));

        out.flush();
        out.close();

    }
}
