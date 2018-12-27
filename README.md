--------------------------------------------------------------------------------------------------------------

					# PRESENTATION

-This program is a famous game board named JUST GET TEN, the purpose of this game is get 10 by fisionning the
cell.

--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------

					# RUN & EXECUTE

-Before execute the program you need to install pygame library for the graphic part, so to do this in
LINUX you have to open the terminal then type :

-install dependencies
		
		sudo apt-get install git python3-dev python3-setuptools python3-numpy python3-opengl \
		libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
		libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
		libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
		xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev

-Grab source

		git clone git@github.com:pygame/pygame.git

-Finally build and install

		cd pygame
		python3 setup.py build
		sudo python3 setup.py install

-Run some tests
		
		python3 -m pygame.tests
		python3 -m pygame.examples.aacircle
		python3 -m pygame.examples.aliens
		python3 -m pygame.examples.freetype_misc
		python3 -m pygame.examples.glcube
		python3 -m pygame.examples.sound
		python3 -m pygame.examples.stars

-Then you have to execute the ui.py file.

--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------

					# LICENSE

-This program is “free software” if the program’s users have the four essential freedoms:

.The freedom to run the program as you wish, for any purpose.
.The freedom to study how the program works, and change it so it does your computing as you wish. Access to 
the source code is a precondition for this.
.The freedom to redistribute copies so you can help your neighbor.
.The freedom to distribute copies of your modified versions to others. By doing this you can give the whole 
community a chance to benefit from your changes. Access to the source code is a precondition for this.
