
[back](api_files.md) 

<a name="how_to_make_api"></a>
### How to make an api file

An api file is a plain text file with one entry per line.

For example, here is an excerpt from the api file for the C standard library,

```
abort();
abs(int n);
acos(double x);
asctime(const struct tm* tp);
```

If use.escapes is enabled, information can span multiple lines, for example,

```
abort() Param: ()\t\nDesc: Abort current process
abs(double x) Param: (Value whose absolute value is returned.)\t\nDesc: Compute absolute value
acos(double x) Param: (Value whose arc cosine is computed, in the interval [-1,+1].)\t\nDesc: Compute arc cosine
```

To generate api files for your own source code, one of these tools may be helpful:

* For C/C++ headers, an api file can be generated using [ctags](http://ctags.sourceforge.net/) and then the [tags2api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/tags2api.py) Python script (which assumes C/C++ source) on the tags file to grab complete multiple line function prototypes. Some common headers surround parameter lists with a __P macro and may have comments. The [cleanapi](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/cleanapi.cc) utility may be used on these files
* For Python modules, there is a [gen_python](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_python_api.py) script
* For Python 3, there is a [gen_python_3](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_python_3_api.py) script
* For Java classes, there is a [ApiBuilder.java](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/java_ApiBuilder.java) program
* For C# classes, use [genapi.cs](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_csgenapi.zip)
* For PHP, use [php-api-generator](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_php-api-generator.zip) or [phpapi.php](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/phpapi.php.txt)

Activate an api file by following the instructions [here](api_files_howto_install_api.md).

To see more advanced settings, search for "calltip" in the [SciTE Documentation](http://www.scintilla.org/SciTEDoc.html).
