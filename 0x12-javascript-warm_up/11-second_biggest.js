#!/usr/bin/node

// Get the arguments passed from the command line
const args = process.argv.slice(2);

// Check if no argument is passed or only one argument is passed
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to integers
  const numbers = args.map(Number);

  // Sort the numbers in ascending order
  const sortedNumbers = numbers.sort((a, b) => a - b);

  // Get the second last element from the sorted array
  const secondLargest = sortedNumbers[sortedNumbers.length - 2];

  // Print the second largest number
  console.log(secondLargest);
}
