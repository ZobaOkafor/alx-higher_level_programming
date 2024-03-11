#!/usr/bin/node

// Check if the first argument exists
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  // Convert the first argument to an integer
  const num = parseInt(process.argv[2], 10);

  // Check if the conversion is successful
  if (!isNaN(num)) {
    console.log('My number: ' + num);
  } else {
    console.log('Not a number');
  }
}
