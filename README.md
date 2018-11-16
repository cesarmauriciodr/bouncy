# ZINA (test)
Technical test for Zina Team / Nokia

### Problem
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

### Prerequisites
 * Python 3.6.5
 * virtualenv

### Installing
Clone or download project from: 
```
https://github.com/cesarmauriciodr/bouncy.git
```

Activate virtualenv
```
virtualenv --python=python3.6 bouncy-env
source bouncy-env/bin/activate
```

Install requirements (for run test), go to project and run
```
pip3 install -r requirements.txt
```

## Run project
go to project and just run:

```
python3 bouncy_main.py <percentage>
```
Enjoy!! =)

## Running the tests
Just run:

```
python3 -m unittest -v bouncy_test.py
```

## Versioning

Use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/cesarmauriciodr/bouncy/tags). 

## Authors

* **Cesar M. Dueñas Ruiz** - *Initial work* - [cesarmauriciodr](https://github.com/cesarmauriciodr)

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [www.mathblog.dk](https://www.mathblog.dk/project-euler-112-density-bouncy-numbers/)
