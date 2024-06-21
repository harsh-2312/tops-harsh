//q15 
/*Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks
in Chem>=50 and Total in all three subject >=190 or Total in Maths and
Physics >=140 -Input the marks obtained in
Physics :65 Input the marks obtained in Chemistry :51 Input the marks
obtained in Mathematics :72 Total marks of Maths, Physics and Chemistry :
188 Total marks of Maths and Physics : 137 The candidate is not eligible.*/

#include<stdio.h>
int main(){

int math, phy , chem, total_marks , math_phy;

    printf("marks of math:");
    scanf("%d", &math);

    printf("marks of phy:");
    scanf("%d", &phy);

    printf("marks of chem:");
    scanf("%d", &chem);
      
    total_marks = math + phy + chem;
    printf("total marks:%d\n",total_marks);
    
    math_phy = math + phy;
    printf("total math & phy marks:%d\n",math_phy);
    

    
    if((math >= 65) && (phy >= 55) && (chem >= 50) && ((total_marks >= 190) || (math_phy >= 140))){

     printf("the candidete is eligible\n");
    }
    else{
        printf("the candidete is not eligible \n");
    }
    printf("thank you \n");
      return 0;
}       