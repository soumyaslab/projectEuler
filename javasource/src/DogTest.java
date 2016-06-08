
public class DogTest {

	String bread;
	int age;
	String color;
	
//	public DogTest(){
//		System.out.println("This is a Dog constructor .. \n");
//	}
//	
	public void barking(){
		System.out.println("Dog is barking ..\n");
	}
	
	public void hungry(){
		System.out.println("Dog in hungry .. \n");
	}
	
	public void sleeping(){
		System.out.println("Dog is sleeping .. \n");
	}
	
//	public DogTest(){
//		System.out.println("This is a Dog constructor .. \n");
//	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DogTest myPuppy = new DogTest();
		
		myPuppy.barking();
		myPuppy.hungry();
		myPuppy.sleeping();
		
	}

}
