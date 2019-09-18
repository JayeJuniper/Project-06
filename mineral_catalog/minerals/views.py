from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.forms.models import model_to_dict
import random
import json

from .models import Mineral


MINERALS = Mineral.objects.all()


def mineral_dict(mineral):
    '''This function composes data entries from minerals.json into individual
    dicts which then are passed into the add_mineral function to and is
    added to the database.'''
    fields = {
        'name': 'N/a',
        'image_filename': 'N/a',
        'image_caption': 'N/a',
        'category': 'N/a',
        'formula': 'N/a',
        'strunz_classification': 'N/a',
        'crystal_system': 'N/a',
        'unit_cell': 'N/a',
        'color': 'N/a',
        'crystal_symmetry': 'N/a',
        'cleavage': 'N/a',
        'mohs_scale_hardness': 'N/a',
        'luster': 'N/a',
        'streak': 'N/a',
        'diaphaneity': 'N/a',
        'optical_properties': 'N/a',
        'refractive_index': 'N/a',
        'crystal_habit': 'N/a',
        'specific_gravity': 'N/a',
        'group': 'N/a'
    }
    for field, value in mineral.items():
        fields[field] = value
    return fields


def add_minerals():
    '''This function adds json entries into the database.'''
    with open('minerals.json', encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            try:
                fields = mineral_dict(mineral)
                Mineral(
                    name=fields['name'],
                    image_filename=fields['image_filename'],
                    image_caption=fields['image_caption'],
                    category=fields['category'],
                    formula=fields['formula'],
                    strunz_classification=fields['strunz_classification'],
                    crystal_system=fields['crystal_system'],
                    unit_cell=fields['unit_cell'],
                    color=fields['color'],
                    crystal_symmetry=fields['crystal_symmetry'],
                    cleavage=fields['cleavage'],
                    mohs_scale_hardness=fields['mohs_scale_hardness'],
                    luster=fields['luster'],
                    streak=fields['streak'],
                    diaphaneity=fields['diaphaneity'],
                    optical_properties=fields['optical_properties'],
                    refractive_index=fields['refractive_index'],
                    crystal_habit=fields['crystal_habit'],
                    specific_gravity=fields['specific_gravity'],
                    group=fields['group']
                ).save()
            except IntegrityError:
                continue


def random_pk():
    pk = random.choice(MINERALS).id
    return Mineral.objects.get(pk=pk)


def mineral_list(request):
    # add_minerals()
    return render(request, 'minerals/mineral_list.html',
                  {
                      'minerals': MINERALS,
                      'random_mineral': random_pk(),
                      })


def mineral_detail(request, pk):
    mineral = model_to_dict(get_object_or_404(Mineral, pk=pk))
    return render(request, 'minerals/mineral_detail.html',
                  {
                      'mineral': mineral,
                      'random_mineral': random_pk(),
                      })
