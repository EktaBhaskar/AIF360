from setuptools import setup, find_packages
from functools import reduce

long_description = """The AI Fairness 360 toolkit is an open-source library to help detect and mitigate bias in machine
learning models. The AI Fairness 360 Python package includes a comprehensive set of metrics for datasets and models to
test for biases, explanations for these metrics, and algorithms to mitigate bias in datasets and models.

We have developed the package with extensibility in mind. This library is still in development. We encourage the
contribution of your datasets, metrics, explainers, and debiasing algorithms."""

version = '0.3.0'

with open("aif360/version.py", 'w') as f:
    f.write('# generated by setup.py\nversion = "{}"\n'.format(version))

extras = {
    'OptimPreproc': ['cvxpy>=1.0'],
    'AdversarialDebiasing': ['tensorflow>=1.13.1,<2'],
    'DisparateImpactRemover': ['BlackBoxAuditing'],
    'LIME': ['lime'],
    'ART': ['adversarial-robustness-toolbox>=1.0.0'],
    'notebooks': ['jupyter', 'tqdm']
}
extras['tests'] = reduce(lambda l1, l2: l1+l2, extras.values(), ['pytest>=3.5'])
extras['docs'] = ['sphinx', 'sphinx_rtd_theme']
extras['all'] = list(reduce(lambda s, l: s.union(l), extras.values(), set()))

setup(name='aif360',
      version=version,
      description='IBM AI Fairness 360',
      author='aif360 developers',
      author_email='aif360@us.ibm.com',
      url='https://github.com/IBM/AIF360',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='Apache License 2.0',
      packages=[pkg for pkg in find_packages() if pkg.startswith('aif360')],
      python_requires='>=3.6',
      install_requires=[
          'numpy>=1.16',
          'scipy>=1.2.0',
          'pandas>=0.24.0',
          'scikit-learn>=0.22',
          'matplotlib',
          'fairlearn==0.4.6',
          'tempeh',
          'xport'
      ],
      extras_require=extras,
      package_data={'aif360': ['data/*', 'data/*/*', 'data/*/*/*']},
      include_package_data=True,
      zip_safe=False)
