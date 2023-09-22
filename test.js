const convert = require('./main.js');

//Kiem thu bang phuong phap bang quyet dinh
test('Test invalid score', () => {
    expect(convert(-1)).toBe('Invalid score');
    expect(convert(11)).toBe('Invalid score');
});

test('Test F score', () => {
    expect(convert(0)).toBe('F');
})

test('Test D score', () => {
    expect(convert(4)).toBe('D');
})

test('Test D+ score', () => {
    expect(convert(5)).toBe('D+');
})

test('Test C score', () => {
    expect(convert(5.5)).toBe('C');
})

test('Test C+ score', () => {
    expect(convert(6.5)).toBe('C+');
})

test('Test B score', () => {
    expect(convert(7)).toBe('B');
})

test('Test B+ score', () => {
    expect(convert(8)).toBe('B+');
})

test('Test A score', () => {
    expect(convert(8.5)).toBe('A');
})

test('Test A+ score', () => {
    expect(convert(10)).toBe('A+');
})

//Kiem thu bang phuong phap phan hoach tuong duong
test('Test invalid score', () => {
    expect(convert(-1)).toBe('Invalid score');
    expect(convert(11)).toBe('Invalid score');
});

test('Test F score', () => {
    expect(convert(0)).toBe('F');
})

test('Test D score', () => {
    expect(convert(4.2)).toBe('D');
})

test('Test D+ score', () => {
    expect(convert(5.3)).toBe('D+');
})

test('Test C score', () => {
    expect(convert(5.9)).toBe('C');
})

test('Test C+ score', () => {
    expect(convert(6.6)).toBe('C+');
})

test('Test B score', () => {
    expect(convert(7)).toBe('B');
})

test('Test B+ score', () => {
    expect(convert(8.3)).toBe('B+');
})

test('Test A score', () => {
    expect(convert(8.7)).toBe('A');
})

test('Test A+ score', () => {
    expect(convert(9)).toBe('A+');
})