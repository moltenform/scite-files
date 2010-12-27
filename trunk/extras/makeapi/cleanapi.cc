/*
 A small utility to remove those nasty "__P(" macros and comments
 from the std libc func prototypes in the api files used by SciTE 
 for calltips and autocompletion...
 
 --Modified on 29/04/2000 to remove #if macros from inside Xlib.h's
 --function prototypes

 #include <std_disclaimer.h>

   "I do not accept responsibility for any effects, adverse or otherwise, 
    that this code may have on you, your computer, your sanity, your dog, 
    and anything else that you can think of. Use it at your own risk."
    
 Usage:
    cleanapi <in.api> <out.api> [OPTIONS]

    Options: -c -> Remove Comments
             -v -> Be (frustratingly :) verbose..
 
 By Deepak S.
 deepaks@operamail.com
*/

#include <fstream.h>
#include <string.h>

int main(int argc, char *argv[])
{
	ifstream inapi;
	ofstream outapi;
	
	bool verbose=false, comments=false, comrem=false;
	
	char aline[512]="", modline[512]="";
	char *pptr, *cptr, *wdptr;
	
	int modnum, i, parcnt=0;
	
	if(argc<3)
	{
		cout<<"Usage: cleanapi <in.api> <out.api>"<<endl;
		return -1;
	}

	inapi.open(argv[1]);
	if(!inapi)
	{
		cout<<"Unable to open input file "<<argv[1]<<endl;
		return -1;
	}
	
	outapi.open(argv[2]);
	if(!outapi)
	{
		cout<<"Unable to open output file "<<argv[2]<<endl;
		return -1;
	}
	
	if(argc>3)
	{
		for(i=3; i<argc; i++)
			if(!strcmp(argv[i], "-v"))
				verbose=true;
			else if(!strcmp(argv[i], "-c"))
				comments=true;
			else
			{
				cerr<<"Bad option!"<<endl;
				return -1;
			}
	}
	
	while(inapi.getline(aline, 511)!=NULL)
	{		
		modnum=0;

		if(comments)
		{
			comrem=false;
			pptr=NULL;
			wdptr=aline;
			while(wdptr && (pptr=strstr(wdptr, "/*"))!=NULL)
			{
				cptr=wdptr;
				while(cptr!=pptr)
					modline[modnum++]=*(cptr++);

				if((pptr=strstr(wdptr, "*/"))!=NULL)
					wdptr=pptr+2;
					
				comrem=true;
			}
			
			while(*wdptr)
				modline[modnum++]=*(wdptr++);
				
			modline[modnum]='\0';
			if(verbose && comrem)
				cout<<"Removed comment(s): \n\""<<aline<<"\" becomes \n\""<<modline<<"\""<<endl;
			strcpy(aline, modline);
			modnum=0;
		}

		if((pptr=strstr(aline, "#if"))!=NULL)
		{
			//Fooling around with pointers is a nice time-pass :)
			cptr=aline;
			while(cptr!=pptr)
				modline[modnum++]=*(cptr++);
			if((cptr=strchr(cptr, ' ')))	//Skip the conditions
			{
				cptr++;
				cptr=strchr(cptr, ' ');
				cptr++;
			}
			pptr=strstr(pptr,"#endif");
			while(cptr!=pptr)
				modline[modnum++]=*(cptr++);
			pptr+=6;
			while(*pptr)
				modline[modnum++]=*(pptr++);
			modline[modnum]='\0';
			if(verbose)
				cout<<"Removed nasty #if: \n\""<<aline<<"\" becomes \n\""<<modline<<"\""<<endl;
			strcpy(aline, modline);
			modnum=0;
		}

		if((pptr=strstr(aline, " __P("))!=NULL)
		{
			parcnt=1;
			cptr=aline;
			while(cptr!=pptr)
				modline[modnum++]=*(cptr++);
			pptr+=4;
			while(parcnt && *pptr)
			{
				pptr++;
				if(*pptr=='(') ++parcnt;
				if(*pptr==')') --parcnt;
			}
			cptr+=5;
			while(cptr!=pptr)
				modline[modnum++]=*(cptr++);
			if(*(cptr+1))
			{
				cptr++;
				while(*cptr)
					modline[modnum++]=*(cptr++);
			}			
			modline[modnum]='\0';
			if(verbose)
				cout<<"Removed nasty macro: \n\""<<aline<<"\" becomes \n\""<<modline<<"\""<<endl;
			strcpy(aline, modline);
		}

		outapi<<aline;
		outapi<<endl;
	}
	
	inapi.close();
	outapi.close();
	cout<<"Finished cleaning "<<argv[1]<<" ..."<<endl;
	
	return 0;
}
