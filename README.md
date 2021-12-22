# 2D-Analysis-And-Optimisation-of-A-Car-Tow-Hook
<p align="justify">
The main aim is to create a stronger object able to hold a car's weight without exceeding the yield stress of Aluminium T6-6061. The part's optimization will be executed by evaluating the effect of a thicker hook and different empty geometrical shapes on our model's performance. 
</p>

<p align="center">
<img width="629" alt="Screen Shot 2021-12-22 at 1 17 33 PM" src="https://user-images.githubusercontent.com/70657426/147084797-4d47f4ef-a50f-498b-8ba9-227301f8cf95.png">
</p>

<p align="justify">
The first subplot shows a sharp decrease of the maximum displacement when increasing the thickness of the hook, decreasing from 1.68 mm to 0.9 mm, hence the increase in deformation scale. Overall, the second subplot illustrates a same tendency for both stresses. The stress located at the critical point of the original design decrease to nearly sixth of its value for the thickest hook (630 to 104 MPa), falling under the yield strength of the material. The maximum stress acting on the new design is located at a force node and decline slightly from 630 to 462 MPa, causing the part to fail. This may be caused by the type of load applied, we used concentrated forces instead of a uniformly distributed pressure ABAQUS.
</p>

<p align="center">
  
![Figure_1](https://user-images.githubusercontent.com/70657426/147084862-aac721b7-1fb0-4367-b1a0-46f7aaa02b94.png)
  
</p>

