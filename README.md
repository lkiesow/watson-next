![watson-next logo](watson-next.svg)

A wonderful CLI to track your time.
===================================

ℹ️ `watson-next` is a fork of the seemingly abandoned [TailorDev/Watson](https://github.com/TailorDev/Watson).

Watson is here to help you manage your time. You want to know how
much time you are spending on your projects? You want to generate a nice
report for your client? Watson is here for you.

Wanna know what it looks like?

[![asciicast](https://asciinema.org/a/35918.svg)](https://asciinema.org/a/35918)

Nice isn't it?

Installation
------------

Install watson-next using pip:

```
$ pip install watson-next
```

Usage
-----

Start tracking your activity via:

```
$ watson start world-domination +cats
```

With this command, you have started a new **frame** for the *world-domination* project with the *cats* tag. That's it.

Now stop tracking you world domination plan via:

```
$ watson stop
Project world-domination [cats] started 8 minutes ago (2016.01.27 13:00:28+0100)
```

You can log your latest working sessions (aka **frames**) thanks to the ``log`` command:

```
$ watson log
Tuesday 26 January 2016 (8m 32s)
      ffb2a4c  13:00 to 13:08      08m 32s   world-domination  [cats]
```

To list all available commands:

```
$ watson help
```

License
-------

Watson-next is released under the MIT License.
See the bundled LICENSE file for details.
