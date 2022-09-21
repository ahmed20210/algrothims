const quick_sort = (arr) => {
  if (arr.length < 2) {
    return arr;
  } else {
    const pivot = arr[0];
    const smaller = arr.filter((el, i) => {
      if (i > 0) {
        return el <= pivot;
      }
    });
    const greater = arr.filter((el, i) => {
      if (i > 0) {
        return el > pivot;
      }
    });
 
    return quick_sort(smaller).concat([pivot].concat(greater));
  }
};
