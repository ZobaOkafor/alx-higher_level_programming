#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => {
    if (current === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
