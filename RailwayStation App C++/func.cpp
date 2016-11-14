#include "header.h"

void Human::setData()
{
	cout << "ÂYour name" << endl;
	cin >> Name;
	cout << "Your surname" << endl;
	cin >> Surname;
}

void Human::getData()
{
	cout << "Owner: ";
	cout << Name << " ";
	cout << Surname << endl;
}

Cashier::Cashier()
{
	string Names[5] = {"Olena", "Larisa", "Olia", "Hrystyna", "Daria"};
	string Surnames[5] = {"Tarasova", "Krasnova", "Lypnyk", "Zhovtun", "Kogut"};
	srand(time(NULL));
	Name = Names[rand()%5-1];
	Surname = Surnames[rand()%5-1];
	srand(time(NULL));
	IdC = rand()%9000+1000;
}

void Cashier::getData()
{
	cout << "Cashier:";
	cout << Name << " ";
	cout << Surname << "   ";
	cout << IdC;
}

SeatA::SeatA()
{
	priceSA=2;
	nplaceSA=0;
}

SeatA::SeatA(int m)
{
	priceSA=2;
	nplaceSA=m;
}

int SeatA::shownplaceSA(int m)
{
	return m;
}

int SeatA::pPriceSA()
{
	return priceSA;
}

SeatB::SeatB()
{
	priceSB=3;
	nplaceSB=0;
}

SeatB::SeatB(int n)
{
	priceSB=3;
	nplaceSB=n;
}

int SeatB::shownplaceSB(int f)
{
	return f;
}

int SeatB::pPriceSB()
{
	return priceSB;
}

Wagon::Wagon()
{
	IdW=00000;
}

WagonA::WagonA()
{
	numberofSA=70;
	numbofWA=0;
}

WagonA::WagonA(int u)
{
	numberofSA=50;
	numbofWA=u;
}

void WagonA::sequel(int p)
{
	sA=seatA->shownplaceSA(p);
}


void WagonA::getnumberofW()
{
	cout<<numbofWA;
}

WagonB::WagonB()
{
	numberofSB=50;
	numbofWB=0;
}

WagonB::WagonB(int y)
{
	numberofSB=50;
	numbofWB=y;
}

void WagonB::sequel(int	q)
{
	sB=seatB->shownplaceSB(q);
}

void WagonB::getnumberofW()
{
	cout<<numbofWB;
}

int Train::numbofW()
{
	int j;
	j=WA->sumofWA()+WB->sumofWB();
	return j;
}

void Train::TId()
{
	srand(time(NULL));
	qTId=rand()%900+100;
	cout<<"²íäåêñ ïîòÿãà: "<<qTId<<endl;
}

void Route::numbofWT(Train* train)
{
	train->numbofW();
}

void Route::timeofTrain()
{
	cout<<time<<endl;
}

void Route::setRoute(string H, string X)
{
	C=H+"."+X;
}

void Route::getRoute()
{
	cout<<"Route: "<<C<<endl;
}

bool Route::route()
{
	string a;
	ifstream F;
	F.open("C://Games//vokzal.txt");
	if(!F)
		cout<<"There is no such a route!\n"<<endl;
	else
	{
		while (!F.eof())
		{
			if(C == a) 
				F>>a>>time>>k;
				return true;
		}
		F.close();
	}
}

int Route::priceA(SeatA* seA)
{
	k=15;
	cout<<"Price: "<<k*seA->pPriceSA()<<endl;
	return 0;
}

int Route::priceB(SeatB* seB)
{
	k=20;
	cout<<"Price: "<<k*seB->pPriceSB()<<endl;
	return 0;
}

void Ticket::setIdTicket()
{
	srand(time(NULL));
	IdTicket=rand()%90000+10000;
}

void Ticket::getIdTicket()
{
	cout<<"Ticket ID: "<<IdTicket<<endl;
}

void Ticket::setData()
{
	do
	{
		cout << "The day of daperture" << endl;
		cin >> day;
	} 
	while (day>31 || day<=0);
	do
	{
		cout<<"The month of departure(numbers)"<<endl;
		cin>>month;
	} 
	while (month>12 || month<=0);
}

void Ticket::getData()
{
	cout<<"ÄDate: "<<day<<"."<<month<<".2015"<<endl;
}

void Ticket::showHuman(Human* human)
{
	human->getData();
}

void Ticket::showRoute(Route* route)
{
	route->getRoute();
}

void Ticket::showCashier(Cashier* cashier)
{
	cashier->getData();
}

void Ticket::showPlaceSA(SeatA* sa, int p)
{
	sa->shownplaceSA(p);
}

void Ticket::showPlaceSB(SeatB* sb, int q)
{
	sb->shownplaceSB(q);
}
