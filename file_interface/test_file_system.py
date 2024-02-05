from file_system import File, SizeLessThanFilter, TypeFilter, apply_filters


def test_apply_filters_when_applied_then_filters_files_correctly():
    files = [
        File(name='image1', location='/home/images', size=10, type='.png'),
        File(name='vid1', location='/home/images/videos', size=100, type='.mov'),
        File(name='image2', location='/home/images', size=3, type='.png'),
        File(name='vid2', location='/home/images/videos', size=2, type='.mov'),
    ]
    
    filters = [
        SizeLessThanFilter(5),
        TypeFilter('.png')
    ]
    
    filtered = apply_filters(files, filters)
    
    assert filtered == [File(name='image2', location='/home/images', size=3, type='.png'),]