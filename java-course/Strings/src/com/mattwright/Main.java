package com.mattwright;

public class Main {

    public static void main(String[] args) {
        // == Primitive Data Types: ==
	    // byte
        // short
        // int
        // long
        // float
        // double
        // char
        // boolean

        // strings are not a primitive data type,
        // but in Java are basically treated like a primitive type,
        // they are technically a class

        String myString = "This is a string";
        System.out.println("myString is equal to = " + myString);
        myString = myString + ", and this is more.";
        System.out.println("myString is equal to = " + myString);
        myString = myString + " \u00A9 2015";
        System.out.println("myString is equal to = " + myString);

        String numberString = "250.55 ";
        numberString = numberString + "49.45";
        System.out.println("The result is " + numberString);

        String lastString = "10";
        int myInt = 50;
        lastString = lastString + myInt;
        System.out.println("LastString is equal to " + lastString);
        double doubleNumber = 120.47;
        lastString = lastString + doubleNumber;
        System.out.println("LastString is equal to " + lastString);
    }
}
