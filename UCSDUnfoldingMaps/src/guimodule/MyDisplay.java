package guimodule;

import processing.core.PApplet;
import processing.core.PImage;

public class MyDisplay extends PApplet {
	
	//Setup method to initialize our window
	public void setup()
	{
		size(400, 400);
		background(255);
		stroke(0);
		//img = loadImage("http://cseweb.ucsd.edu/~minnes/palmTrees.jpg", "jpg");
		//img.resize(0, height);			//resize the image
		//image(img, 0, 0); 				//display image
		
	}
	
	//Draw on the window that we just setup
	public void draw()
	{
		int[] color = sunColorSec(second());
		fill(color[0], color[1], color[2]);
		ellipse(width/4, height/5, width/4, height/5);
	}
	
	public int[] sunColorSec(float seconds)
	{
		int[] rgb = new int[3];
		// Scale the brightness of the yellow based on the seconds. 0 seconds
		// is black. 30 seconds is bright yellos.
		float diffFrom30 = Math.abs(30-seconds);
		
		float ratio = diffFrom30/30;
		rgb[0] = (int)(255*ratio);
		rgb[1] = (int)(255*ratio);
		rgb[2] = 0;
		
		return rgb;
	}
	
}
