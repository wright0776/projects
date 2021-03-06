package com.mattwright;

public class Main {

    public static void main(String[] args) {
        // width of int = 32 (4 bytes).
	    int myIntValue = 5 / 2;
	    // width of float = 32 (4 bytes).
	    float myFloatValue = 5f / 3f;
	    // width of double - 64 (8 bytes).
	    double myDoublealue = 5d / 3d;

        System.out.println("myIntValue = " + myIntValue);
        System.out.println("myFloatValue = " + myFloatValue);
        System.out.println("myDoubleValue = " + myDoublealue);

        // Convert a given number of pounds to kilograms
        // 1. Create a variable to store the number of pounds
        // 2. Calculate the number of kilograms for the number above and store in a variable.
        // 3. Print out the result.
        //
        // NOTES: 1 pound is equal to 0.45359237 kilograms.

        double pounds = 145d;
        double kgs = 65d;
        double numberOfKgs = pounds * 0.45359237d;
        double numberOfLbs = kgs / 0.45359237d;
        System.out.println("numberOfKgs = " + numberOfKgs);
        System.out.println("numberOfLbs = " + numberOfLbs);

        double pi = 3.141_592_654d;
    }
}
