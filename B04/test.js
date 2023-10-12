//Test for B04.js

const calculateGPA = require('./B04.js');

test('Test invalid input', () => {
    expect(calculateGPA([])).toBe('Invalid input');
});

test('Test invalid score', () => {
    expect(calculateGPA([{score: 11, credits: 4}])).toBe('Invalid score');
});

test('Test score', () => {
    expect(calculateGPA([{score: 9, credits: 4}])).toBe(9);
});
