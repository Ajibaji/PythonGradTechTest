import pytest

def createMenuData(data):
    # insert your code here

    return data




def test_actualResult():
    expectedResult = [
            {
              "title": "parent1",
              "data": ["parent1child", "parent1child2", "parent1child3"]
            },
            { "title": "parent2", "data": ["parent2child", "parent2child2"] },
            { "title": "parent3", "data": ["parent3child1"] }
          ]

    data = [
        "parent1/parent1child",
        "parent1/parent1child2",
        "parent2/parent2child",
        "parent2/parent2child2",
        "parent1/parent1child3",
        "parent3",
        "parent3/parent3child1",
        "parent4"
      ]

    assert cmp(createMenuData(data), expectedResult) == 0
