# briefcase docker

The [Beeware](https://beeware.org/) python package based on Ubuntu 16.04, used in particular to run the `briefcase` command.

## Motivations

> Packaging binaries for Linux is complicated, because of the inconsistent library versions present on each distribution. Briefcase uses the AppImage format by default, which resolves many of these problems. An AppImage can be executed on any Linux distribution with a version of libc greater than or equal the version of the distribution where the AppImage was created.
>
> To simplify the packaging process, Briefcase provides a pre-compiled Python support library. This support library was compiled on Ubuntu 16.04, which means the AppImages build by Briefcase can be used on any Linux distribution of about the same age or newer - but those AppImages must be compiled on Ubuntu 16.04.

-- [Beeware tutorial](https://docs.beeware.org/en/latest/tutorial/tutorial-3.html)

## Usage

For instance if you want to run the `briefcase create` command in your project:

```
sudo docker run -v $(pwd):/project -i roipoussiere/briefcase create
```
