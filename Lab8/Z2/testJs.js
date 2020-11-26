var expect = chai.expect;

describe('The cyfry() function', function () {

    it('Cyfry', function () {
        expect(numbers("111")).to.equal(3);
        expect(numbers("aaa")).to.equal(0);
        expect(numbers("aaa111")).to.equal(3);
        expect(numbers("111aaa")).to.equal(3);
        expect(numbers("")).to.equal(0);
    });
});

describe('The litery() function', function () {

    it('Litery', function () {
        expect(letters("111")).to.equal(0);
        expect(letters("aaa")).to.equal(3);
        expect(letters("aaa111")).to.equal(3);
        expect(letters("111aaa")).to.equal(3);
        expect(letters("")).to.equal(0);
    });
});

describe('The suma() function', function () {

    it('Suma', function () {
        expect(summ("111")).to.equal(111);
        expect(summ("aaa")).to.equal(111);
        expect(summ("aaa111")).to.equal(111);
        expect(summ("111aaa")).to.equal(222);
        expect(summ("")).to.equal(222);
    });
});
