function calculateGPA(score) {
    if (!score || score.length === 0) {
        return 'Invalid input'
    }
    let sumOfScore = 0;
    let sumOfCredits = 0
    for (let i = 0; i < score.length; i++) {
        if (score[i].score < 0 || score[i].score > 10) {
            return 'Invalid score';
        }

        sumOfScore += score[i].score * score[i].credits;
        sumOfCredits += score[i].credits;
    }
    const result = parseFloat((sumOfScore / sumOfCredits).toFixed(2));
    return result
}

// console.log(calculateGPA([{score: 9, credits: 4}]));

module.exports = calculateGPA;