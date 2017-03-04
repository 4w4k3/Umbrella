# Umbrella Dropper

Copyright 2017 Umbrella
Written by: * **Alisson Moretto** - [4w4k3](https://github.com/4w4k3)

Umbrella is a file dropper dedicated to pentest, its download files on target system are execute them without a double execution of exe, only of embed.

To compromise the same target again, you need delete this folder on target system : - C:\Users\Public\Libraries\Intel - because dropper checks the existence of her to take a decision of what be do.

Twitter: @4w4k3Official

## DISCLAIMER: 

"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
Taken from [LICENSE](LICENSE).

## Features 

- Download executable on target system.
- Silent execution.
- Download and execute executable once time.
- If the exe already had downloaded and running, open only pdf/docx/xxls/jpg/png.
- Some Phishing methods are included.
- Multiple Session disabled.
- Bypass UAC.

### Needed dependencies

* apt
* wine
* wget
* Linux
* sudo access
* python2.7
* python 2.7 on Wine Machine

### Tested on:

+ Kali Linux - SANA
+ Kali Linux - ROLLING
+ Ubuntu 14.04-16.04 LTS
+ Debian 8.5
+ Linux Mint 18.1
+ Black Arch Linux

### Cloning:
```
git clone https://github.com/4w4k3/Umbrella.git
```

### Running:
```
sudo python umbrella.py
```

If you have another version of Python:

```
sudo python2.7 umbrella.py
```

### Screenshot:
![Shot](https://github.com/4w4k3/Umbrella/blob/master/Screens/shot.png)

More in [Screens](Screens)

### Contribute:
Send me more features if you want it :D

### Contact:
**4w4k3@protonmail.com**

## License:

This project is licensed under the BSD-3-Clause - see the [LICENSE](LICENSE) file for details.
