package com.mattwright;

public class Main {

    public static void main(String[] args) {
	    char myChar = '\u00A9';
        System.out.println("Unicode output was: " + myChar);

        boolean myBoolean = true;
        boolean isMale = true;

        // 1. Find the code for the registered symbol on the same line as the copyright symbol.
        // 2. Create a variable of type char and assign it the unicode value for that symbol.
        // 3. Display it on the screen.

        char registered = '\u00AE';
        System.out.println("Output is: " + registered);
    }
}
