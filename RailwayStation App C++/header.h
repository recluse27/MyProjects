#include <iostream>
#include <locale>
#include <string>
#include <cstdlib>
#include <ctime>
#include "windows.h"
#include <fstream>

using namespace std;
	
class Human
{
protected: 
	string Name, Surname;
public:
	void setData();
	virtual void getData();
};

class Cashier : public Human
{
private: 
	int IdC;
public: 
	Cashier();
	void getData();
};

class SeatA
{
private:
	int priceSA, nplaceSA;
public:
	SeatA();
	SeatA(int);
	int shownplaceSA(int);//
	int pPriceSA();
};

class SeatB
{
private:
	int priceSB, nplaceSB;
public:
	SeatB();
	SeatB(int);
	int shownplaceSB(int f);
	int pPriceSB();
};

class Wagon
{
protected: 
	int IdW;
public:
	Wagon();
	virtual void getnumberofW() = 0;
};

class WagonA : public Wagon
{
private:
	SeatA* seatA;
	int numberofSA;
	int numbofWA;
	int sA;
public:
	WagonA();
	WagonA(int);
	void getnumberofW();
	int sumofWA(){return 5;};
	void sequel(int);
};

class WagonB : public Wagon
{
private:
	SeatB* seatB;
	int numberofSB;
	int numbofWB;
	int sB;
public:
	WagonB();
	WagonB(int);
	void getnumberofW();
	int sumofWB(){return 5;};
	void sequel(int);
};

class Train
{
protected: 
	int numbofWagon, qTId;
private:
	WagonA* WA;
	WagonB* WB;
public:
	int numbofW();
	void TId();
};

class Route
{
private:
	string C, time;
	int k;
public:
	void setRoute(string, string);
	void getRoute();
	bool route();//
	void numbofWT(Train*);
	void timeofTrain();
	int priceA(SeatA*);
	int priceB(SeatB*);
};

class  Ticket
{
private:
	int IdTicket;
	int day,month;
public:
	void setIdTicket();
	void getIdTicket();
	void setData();
	void getData();
	void showHuman(Human*);
	void showRoute(Route*);
	void showCashier(Cashier*);
	void showTrainTime(Route*);
	void showPlaceSA(SeatA*, int p);
	void showPlaceSB(SeatB*, int q);
};
