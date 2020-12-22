from django.urls import reverse
from rest_framework.test import APITestCase


class ViewsTestCase(APITestCase):
    fixtures = ["populate_db.json"]

    def test_showcase_all_sucess(self):
        response = self.client.get(
            reverse("showcase-list"), {"page_routes": []}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_showcase_all_failure(self):
        response = self.client.get(
            reverse("showcase-list"), {"page_routes": "Mock"}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_showcase_page_routes_unique(self):
        response = self.client.get(
            reverse("showcase-list"), {"page_routes": ["/destinos"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_showcase_page_routes_multiple(self):
        response = self.client.get(
            reverse("showcase-list"), {"page_routes": ["/destinos", "/"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_itens_showcase_city_unique(self):
        response = self.client.get(
            reverse("showcase-list"), {"target_citys": ["Florianópolis"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_city_multiple(self):
        response = self.client.get(
            reverse("showcase-list"),
            {"target_citys": ["Florianópolis", "Iraí"]},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_state_unique(self):
        response = self.client.get(
            reverse("showcase-list"), {"target_states": ["SC"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_state_multiple(self):
        response = self.client.get(
            reverse("showcase-list"), {"target_states": ["SC", "RS"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_state_unique(self):
        response = self.client.get(
            reverse("showcase-list"), {"target_countrys": ["Brasil"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_state_multiple(self):
        response = self.client.get(
            reverse("showcase-list"),
            {"target_countrys": ["Brasil", "Peru"]},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_category_unique(self):
        response = self.client.get(
            reverse("showcase-list"), {"target_category": ["Hospedagem"]}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_category_multiple(self):
        response = self.client.get(
            reverse("showcase-list"),
            {"target_category": ["Hospedagem", "Hostel"]},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_limit(self):
        response = self.client.get(
            reverse("showcase-list"), {"itens_limit": 2}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_price_order_crescent(self):
        response = self.client.get(
            reverse("showcase-list"), {"itens_price_order": "crescent"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})

    def test_itens_showcase_price_order_decrescent(self):
        response = self.client.get(
            reverse("showcase-list"), {"itens_price_order": "decrescent"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, {})
