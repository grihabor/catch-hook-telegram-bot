def test_mapping_yml():
    from catchbot import config
    
    assert config.load_mapping()
