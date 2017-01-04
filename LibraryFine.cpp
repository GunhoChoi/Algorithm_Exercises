#include <iostream>
using namespace std;

int main(){
	int Actual[3]={0};//0 Day 1 Month 2 Year
	int Expected[3]={0};
	int fine=0;

	for(int i=0; i<3; i++){
		cin >> Actual[i];	
	}

	for(int i=0; i<3; i++){
		cin >> Expected[i];	
	}

	//cout << Actual[0]<< Actual[1] << Actual[2]<< Expected[0]<< Expected[1]<< Expected[2] << endl;

	if (Actual[2]>Expected[2]){fine=10000;}
	else if(Actual[2]<Expected[2]){fine=0;}
	else{
		if (Actual[1]>Expected[1]){fine=500*(Actual[1]-Expected[1]);}
		else if(Actual[1]<Expected[1]){fine=0;}
		else{
			if (Actual[0]>Expected[0]){fine=15*(Actual[0]-Expected[0]);}
			else if(Actual[0]<Expected[0]){fine=0;}
			else{fine=0;}
		}
	}

	cout<< fine << endl;
	return 0;
}