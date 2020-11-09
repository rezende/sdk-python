import starkbank
from unittest import TestCase, main
from tests.utils.brcodePayment import generateExampleBrcodePaymentsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleBrcodePaymentsJson(n=5, next_day=True)
        payments = starkbank.boletopayment.create(payments)
        for payment in payments:
            print(payment)


class TestBoletoPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.boletopayment.query(limit=10))
        print(payments)
        self.assertEqual(10, len(payments))


class TestBoletoPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.boletopayment.query()
        payment_id = next(payments).id
        payment = starkbank.boletopayment.get(id=payment_id)


if __name__ == '__main__':
    main()
