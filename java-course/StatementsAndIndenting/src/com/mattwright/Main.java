package com.mattwright;

public class Main {

    public static void main(String[] args) {
	    int myVariable = 50; // a statement is the entire line -> int myVariable = 50;
        myVariable++; // entire line is a statement;
        myVariable--; // entire line is a statement;

        System.out.println("This is" +
                " another" +
                " still more."
                );

        int anotherVariable = 50; myVariable--; System.out.println("This is another one");
    }
}
