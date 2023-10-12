const calculateGPA = require('./B05.js');

test('Test invalid input', () => {
    expect(calculateGPA([])).toBe('Invalid input');
});

test('Test invalid score', () => {
    expect(calculateGPA([{score: 11, credits: 4}])).toBe('Invalid score');
});

test('Test success', () => {
    expect(calculateGPA([{score: 9, credits: 3}])).toBe(9);
});