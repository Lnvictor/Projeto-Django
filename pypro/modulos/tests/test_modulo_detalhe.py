import pytest
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo():
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    return client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))


def test_titulo_do_modulo(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulos:Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo):
    assert_contains(resp, modulo.publico)
