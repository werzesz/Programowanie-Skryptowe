var assert = chai.assert;

describe('funkcja numbers()', function () {
    it('Dla tekstu: "1(NEWLINE)2(NEWLINE)2(NEWLINE)44(NEWLINE)44(NEWLINE)44"', function () {
        var text = "1\n2\n3\n44\n44\n44\n";
        assert.equal(numbers(text, false), " 44 4, 5, 6 2 2 1 1 3 3");
    });
});

describe('funkcja numbers(), checkbox ', function () {
    it('Dla tekstu: "1(NEWLINE)2(NEWLINE)2(NEWLINE)44(NEWLINE)44(NEWLINE)44"', function () {
        var text = "1\n2\n3\n44\n44\n44\n";
        assert.equal(numbers(text, true), " 44 4, 5, 6, 10, 11, 12 2 2, 8 1 1, 7 3 3, 9");
    });
});

describe('funkcja letters() ', function () {
    it('Dla tekstu: "aa(NEWLINE)aa(NEWLINE)bb(NEWLINE)bb(NEWLINE)a(NEWLINE)b"', function () {
        var text = "aa\naa\nbb\nbb\na\nb\n";
        assert.equal(letters(text, false), " b 1 bb 2 aa 2 a 1");
    });

});
describe('funkcja letters(), checkbox  ', function () {
    it('Dla tekstu: "aa(NEWLINE)aa(NEWLINE)bb(NEWLINE)bb(NEWLINE)a(NEWLINE)b"', function () {
        var text = "aa\naa\nbb\nbb\na\nb\n";
        assert.equal(letters(text, true), " b 2 bb 4 aa 4 a 2");
    });

});