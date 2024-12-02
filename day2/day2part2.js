const fs = require('fs');
const input = fs.readFileSync('day2/example.txt', 'utf8').split('\n');
let count = 0;

const isValidSequence = (numbers) => {
    const wasDescending = Number(numbers[0]) > Number(numbers[1]);
    for (let i = 0; i < numbers.length - 1; i++) {
        const diff = Number(numbers[i]) - Number(numbers[i + 1]);
        wasDescending ? diff < 0 : diff > 0;
        if (diff === 0 || Math.abs(diff) > 3) return false;
        if (wasDescending && diff < 0) return false;
        if (!wasDescending && diff > 0) return false;
    }
    return true;
}

const checkNumbers = (numbers) => {
    if (isValidSequence(numbers)) return true;

    for (let i = 0; i < numbers.length; i++) {
        const newNumbers = [...numbers.slice(0, i), ...numbers.slice(i + 1)];
        if (isValidSequence(newNumbers)) return true;
    }
    return false;
}

input.forEach((line) => {
    const numbers = line.split(' ');
    if (checkNumbers(numbers)) {
        count++;
    }
});

console.log(count);