#include<iostream>
using namespace std;
int partition(int a[],int start, int end){
	int p=start;
	int q=end;
	int x=a[start];
	int i=p;
	for(int j=p+1;j<=q;j++){
		if(a[j]<=x){
			i++;
			swap(a[i],a[j]);
		}
	}
	swap(a[i],a[p]);
	return i;
}
int quicksort(int a[],int start,int end){
	if(start>=end){
		return 0;
	}
	int p= partition(a,start,end);
	quicksort(a,start,p-1);
	quicksort(a,p+1,end);
	return 0;
}
int main(){
    int a[]={5,10,3,6,9,2,11,4};
    int n=8;
    cout<<"Unsorted array"<<endl;
    for(int i=0;i<n;i++){
    	cout<<a[i]<<endl;
	}
	quicksort(a,0,n-1);
	cout<<endl;
	cout<<"Sorted array"<<endl;
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;	
}