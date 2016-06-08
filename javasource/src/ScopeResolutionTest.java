
public class ScopeResolutionTest {
	public String name;
	private double salary;
	
	public void ageTest(){
		int age;
		age = 30;
		System.out.println("The age is: " + age);
	}
	public static void main(String[] args) {
		ScopeResolutionTest test = new ScopeResolutionTest();
		test.ageTest();
		// TODO Auto-generated method stub

	}

}
