# Normal Depth Calculation Application

This application calculates the normal depth for uniform flow in an open rectangular channel using Manning's equation. It uses a graphical user interface (GUI) created with Python Tkinter GUI library.

## Features
- GUI for entering parameters
- Calculation of normal depth iteratively.
- Display of the iteration count and the resulting normal depth.
- Error handling to ensure numerical inputs.


## Manning's equation
![image](https://github.com/user-attachments/assets/0d4b6460-2aed-4733-95f1-17efddc2f1b7)

where:
- Q = Flow rate (m³/s)
- A = Cross-sectional area of flow (m²) 
- R= Hydraulic radius (m), defined as , where P is the wetted perimeter (m).
- J = Slope of the channel bed 
- n = Manning's roughness coefficient

The application iteratively adjusts the normal depth until the left part of the equation matches the right part within a specified tolerance.

## Usage
Once you run the script, a graphical window will appear with the following input fields:
- Slope value (J): Enter the slope of the channel.
- Manning's n: Enter the Manning's roughness coefficient.
- Flow (Q): Enter the flow in cubic meters per second (m³/s).
- Width (b): Enter the channel width in meters.

After entering these values, click the Calculate button to begin the calculation. The application will iteratively adjust the normal depth until the result converges within a specified tolerance.
The normal depth will be displayed in the "Calculated normal depth" field, along with the iteration count.

## Example
To use the application:
Input the following values:
-	Slope (J): 0.00025
-	Manning's n: 0.013
-	Flow (Q): 6 m³/s
-	Width (b): 3 m

Click the Calculate button. The normal depth will be calculated and displayed.
