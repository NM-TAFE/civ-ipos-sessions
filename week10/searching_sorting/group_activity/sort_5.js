function sort5(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  let pivot = arr[0];
  let lessThanPivot = arr.slice(1).filter((x) => x <= pivot);
  let greaterThanPivot = arr.slice(1).filter((x) => x > pivot);

  return [...sort5(lessThanPivot), pivot, ...sort5(greaterThanPivot)];
}

// Example usage
console.log(sort5([64, 34, 25, 12, 22, 11, 90]));
