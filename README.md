# NIC (National Identity Card) Information Extractor

This Python program extracts information from a Sri Lankan National Identity Card (NIC) number. It provides the user's birthday, day of the week they were born, and their gender.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Functions](#functions)
  - [Validation](#validation)
  - [Identify Born Year](#identify-born-year)
  - [Get Born Date](#get-born-date)
  - [Get Gender](#get-gender)
- [User Input](#user-input)
- [Output](#output)

## Introduction

This Python program takes a Sri Lankan National Identity Card (NIC) number as input and extracts information such as the user's birthday, the day of the week they were born, and their gender.

## Requirements

- Python 3.x

## How to Use

1. Run the script in a Python environment.
2. Enter your NIC number when prompted.
3. The program will validate the NIC number and extract information about your birthday, the day you were born, and your gender.

## Functions

### Validation

The `validate` function checks if the NIC number is valid by ensuring it is exactly 12 digits and contains only numeric characters.

### Identify Born Year

The `get_born_year` function extracts the birth year from the NIC number.

### Get Born Date

The `get_born_date` function calculates the exact birth date based on the NIC number.

### Get Gender

The `get_gender` function determines the gender based on the NIC number.

## User Input

The user is prompted to enter their NIC number. The program validates the input to ensure it is a valid NIC number.

## Output

The program outputs the user's birthday, the day of the week they were born, and their gender based on the NIC number.

Feel free to contribute, report issues, or suggest improvements!

