package com.MattWright;

public class Main {

    public static void main(String[] args) {

        // in has a width of 32
        int myMinValue = -2_147_483_648; // a literal
        int myMaxValue = 2_147_483_647; // a literal
        int myTotal = (myMinValue / 2);
        System.out.println("myTotal " + myTotal);

        // byte has a width of 8
        byte myByteValue = -128;
        byte myMaxByteValue = 127;
        byte myNewByteValue = (byte) (myByteValue / 2);
        System.out.println("myNewByteValue = " + myNewByteValue);

        // short has a width of 16;
        short myShortValue = -32_768;
        short myMaxShortValue = 32_767;
        short myNewShortValue = (short) (myShortValue / 2);
        System.out.println("myNewShortValue = " + myNewShortValue);

        // long has a width of 64;
        long myLongValue = 100L;
        long myMinLongValue = -9_223_372_036_854_775_808L;
        long myMaxLongValue = 9_223_372_036_854_775_807L;


        byte byteValue = 86;
        short shortValue = 25_000;
        int intValue = 1_888_999_555;
        long longTotal = 50000L + 10L * (byteValue + shortValue + intValue);
        short shortTotal = (short) (1000 + 10 * (byteValue + shortValue + intValue));
        System.out.println("longTotal = " + longTotal);
        System.out.println("shortTotal = " + shortValue);


    }
}
