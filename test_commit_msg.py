from commit_msg import is_valid


def test_is_valid_commit_message_no_body():
    valid_commit_message = "docs: correct spelling of CHANGELOG"
    assert is_valid(valid_commit_message), "Message Should Be Valid"


def test_is_valid_commit_message_with_scope():
    valid_commit_message = "feat(lang): add polish language"
    assert is_valid(valid_commit_message), "Message Should Be Valid"


def test_is_valid_commit_message_with_issue_number():
    valid_commit_message = """fix: correct minor typos in code

    see the issue for details on the typos fixed

    closes issue #12"""
    assert is_valid(valid_commit_message), "Message Should Be Valid"


def test_is_valid_commit_message_with_description_and_breaking_change():
    valid_commit_message = """feat: allow provided config object to extend other configs

    BREAKING CHANGE: `extends` key in config file is now used for extending other config files"""
    assert is_valid(valid_commit_message), "Message Should Be Valid"


def test_is_valid_commit_message_with_exclamation_mark_to_draw_attention_to_breaking_change():
    valid_commit_message = """chore!: drop Node 6 from testing matrix

    BREAKING CHANGE: dropping Node 6 which hits end of life in April"""
    assert is_valid(valid_commit_message), "Message Should Be Valid"


def test_is_invalid_with_non_conventional_commit():
    valid_commit_message = """add new change to code"""
    assert not is_valid(valid_commit_message), "Message Should Be Invalid"


def test_is_invalid_with_improper_type():
    valid_commit_message = """some_improper_type: correct spelling of CHANGELOG"""
    assert not is_valid(valid_commit_message), "Message Should Be Invalid"
