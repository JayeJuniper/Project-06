from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abernathyite",
            image_caption="Pale yellow abernathyite crystals and green..."
        )
        self.mineral2 = Mineral.objects.create(
            name="test name",
            image_caption="test caption"
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral.name, resp.context['mineral'].values())
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
