import pytest


@pytest.mark.parametrize('mapping,json_obj,expected', [
    ({}, {}, {}),
    ({'name': 'obj.name'}, {'obj': {'name': 'John'}}, {'name': 'John'}),
    ({
         'user': {
             'id': 'project.user_id',
             'name': 'project.user_name'
         },
         'name': 'project.name'
     }, {
         'project': {
             'user_id': 2574,
             'user_name': 'Dan',
             'name': 'coolbot',
         }
     }, {
         'user': {
             'id': 2574,
             'name': 'Dan'
         },
         'name': 'coolbot'
     }),
])
def test_static_content(mapping, json_obj, expected):
    from catchbot.message.content import get_static_msg_content

    assert expected == get_static_msg_content(mapping, json_obj)
