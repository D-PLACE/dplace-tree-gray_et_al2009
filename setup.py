from setuptools import setup


setup(
    name='cldfbench_gray_et_al2009',
    py_modules=['cldfbench_gray_et_al2009'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'gray_et_al2009=cldfbench_gray_et_al2009:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
