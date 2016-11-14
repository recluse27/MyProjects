#include "header.h"

int main ()
{
	ñout<<"Welcome to Kyiv Railway Station"<<endl;
	Human h1;
	h1.setData();
	h1.getData();
	
	Cashier c1;

	string A, B;
	
	cout<<"Start city"<<endl;
	cin>>A;
	cout<<"End city"<<endl;
	cin>>B;

	Route r1;
	r1.setRoute(A,B);
	r1.route();
	if(r1.route()==true)
	{	
		Train t1;

		int i;
		cout<<"Type 1:2nd comfort class\n";
		cout<<"Type 2:1st comfort class\n";
		cin>>i;
		if(i==1) {
			Ticket tickA;
			int e;
			int p;
			do
			{
				cout<<"Choose your wagon (from 1 to 5)"<<endl;
				cin>>e;
			} 
			while (e>5 || e<=0);
			WagonA wagA(e);
			do
			{
				cout<<"Choose your place (from 1 to 70)"<<endl;
				cin>>p;
			} 
			while (p>70 || p<=0);
			SeatA seatA(p);
			seatA.shownplaceSA(p);
			wagA.sequel(p);
			tickA.setIdTicket();
			tickA.setData();
			t1.numbofW();
			seatA.pPriceSA();
			cout<<"Your ticket:"<<endl;
			tickA.getIdTicket();
			tickA.getData();
			tickA.showHuman(&h1);
			r1.priceA(&seatA);
			cout<<"Place: "<<p<<endl;
			cout<<"Wagon: "<<e<<endl;
			t1.TId();
			tickA.showPlaceSA(&seatA,p);
			r1.getRoute();
			c1.getData();
		}
		else if(i==2){
			Ticket tickB;
			int o;
			int q;
			do
			{
				cout<<"Choose your wagon (from 1 to 5)"<<endl;
				cin>>o;
			} 
			while (o>5 || o<=0);
			WagonB wagB(o);
			do
			{
				cout<<"Choose your place (from 1 to 50)"<<endl;
				cin>>q;
			} 
			while (q>50 || q<=0);
			SeatB seatB(q);
			seatB.shownplaceSB(1);
			wagB.sequel(q);
			tickB.setIdTicket();
			tickB.setData();
			t1.numbofW();
			seatB.pPriceSB();
			cout<<"Your ticket:"<<endl;
			tickB.getIdTicket();
			tickB.getData();
			tickB.showHuman(&h1);
			r1.priceB(&seatB);
			cout<<"Place: "<<q<<endl;
			cout<<"Wagon: "<<o<<endl;
			t1.TId();
			tickB.showPlaceSB(&seatB,q);
			r1.getRoute();
			c1.getData();
		}
	}
	else 
		cout << "Òhere is no such a route!";
	
	cin.get();
	cin.get();
    return 0;
}
