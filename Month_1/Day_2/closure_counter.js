function createCounter() {
  let count = 0;

  return {
    increment: function () {
        count ++
    },

    decrement: function () {
        count --
    },

    reset: function () {
        count = 0;
    },

    getCount: function () {
        return count;
    },
  };
}

const counter = createCounter();

console.log("Initial Count:", counter.getCount());

counter.increment();
console.log("After Increment:", counter.getCount());

counter.increment();
console.log("After Increment:", counter.getCount());

counter.decrement();
console.log("After Decrement:", counter.getCount());

counter.reset();
console.log("After Reset:", counter.getCount());


const counterA = createCounter();
const counterB = createCounter();

counterA.increment();
console.log("Counter A Count:", counterA.getCount());

counterB.increment();
console.log("Counter B Count:", counterB.getCount());