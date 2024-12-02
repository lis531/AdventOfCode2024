const fs = require('fs');
const input = fs.readFileSync('day2/example.txt', 'utf8').split('\n');
let count = 0;

input.forEach((line) => {
    let wasAscending = null;
    const numbers = line.split(' ');

    for (let i = 0; i < numbers.length - 1; i++) {
        const current = Number(numbers[i]);
        const next = Number(numbers[i + 1]);
        if (current < next) {
            if (wasAscending === null) {
                wasAscending = true;
            } else if (wasAscending === false) {
                return;
            }
        } else if (current > next) {
            if (wasAscending === null) {
                wasAscending = false;
            } else if (wasAscending === true) {
                return;
            }
        }
        if (Math.abs(current - next) > 3 || current - next === 0) {
            return;
        }
    }
    count++;
});

console.log(count);