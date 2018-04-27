package kr.gudi;

import java.io.IOException;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Main extends HttpServlet{

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
	
		System.out.println("doGet : Main");
		getParam(req);
	}

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		System.out.println("doPost");
		req.setCharacterEncoding("utf-8"); //Post방식으로 값을 받았을 때 한글이 깨지는것을 방지하기 위한 메서드.
		getParam(req);
	}

	void getParam(HttpServletRequest req) {
		Enumeration<String> names = req.getParameterNames();
		while(names.hasMoreElements()) {
			
			String paramName = (String) names.nextElement();
			
			String value = req.getParameter(paramName);
			System.out.println(paramName + " : " + value);
			
		}
	}

}
