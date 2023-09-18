function convert(score) {
    if (score < 0 || score > 10) {
        return 'Invalid score';
    }

    if (score >= 0 && score < 4) {
        return 'F';
    } else if (score >= 4 && score < 5) {
        return 'D';
    } else if (score >= 5 && score < 5.5) {
        return 'D+';
    } else if (score >= 5.5 && score < 6.5) {
        return 'C';
    } else if (score >= 6.5 && score < 7) {
        return 'C+';
    } else if (score >= 7 && score < 8) {
        return 'B';
    } else if (score >= 8 && score < 8.5) {
        return 'B+';
    } else if (score >= 8.5 && score < 9) {
        return 'A';
    } else {
        return 'A+';
    }
}

module.exports = convert;