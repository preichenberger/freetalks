Freetalks
=========

Freetalks is a catalog of free talks and lectures.

### Development

Disable deprecation warnings (add to top of nosetests):

    import warnings
    warnings.filterwarnings('ignore', category=DeprecationWarning)

Run tests:

    alias gaetest="nosetests --with-gae --gae-lib-root=$HOME/.lib/google_appengine/"
    gaetest

To setup development data go to the [Development Console][console] and run the following:

    from tests.fixtures import dataset
    dataset.clear()
    dataset.setup()

### Licenses

This work is licensed under the MIT License (see the LICENSE file).

[console]: http://localhost:8080/_ah/admin/interactive
