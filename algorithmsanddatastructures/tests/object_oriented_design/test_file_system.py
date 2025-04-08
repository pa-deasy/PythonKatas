from object_oriented_design.file_system import Directory, File


def test_number_of_files_when_counted_then_returns_expected_count():
    dir_a = Directory(name='a', parent=None, entries=[])
    file_a_1 = File(name='a1', parent=dir_a, size=1)
    file_a_2 = File(name='a2', parent=dir_a, size=2)
    file_a_3 = File(name='a3', parent=dir_a, size=3)
    dir_a.add_entries([file_a_1, file_a_2, file_a_3])

    dir_b = Directory(name = 'b', parent=dir_a, entries=[])
    file_b_1 = File(name='b1', parent=dir_b, size=10)
    file_b_2 = File(name='b2', parent=dir_b, size=20)
    file_b_3 = File(name='b3', parent=dir_b, size=30)
    dir_b.add_entries([file_b_1, file_b_2, file_b_3])

    dir_a.add_entries([dir_b])

    file_count = dir_a.number_of_files()
    
    assert file_count == 7
    